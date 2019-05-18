import axios from 'axios'
import lunr from 'lunr'

export default {
    namespaced: true,
    state: {
        businesses: [],
        geographicBounds: null,
        searchIndex: null,
        searchResults: [],
        searchText: '',
        isLoadingTags: false,
        tags: []
    },
    getters: {
        filteredStores(state) {
            if (state.searchText.length > 0) {
                const filteredBusinesses = [];

                for (let searchResult of state.searchResults) {
                    for (let business of state.businesses) {
                        for (let gameStore of business.stores) {
                            const latLng = L.latLng(parseFloat(gameStore.lat), parseFloat(gameStore.lng));
                            if (parseInt(searchResult.ref) === gameStore.id &&
                                state.geographicBounds &&
                                state.geographicBounds.contains(latLng)) {
                                const obj = Object.assign(gameStore);
                                obj.distanceToCenterPoint = 1.0;
                                obj.business = business;
                                obj.searchResult = Object.assign(searchResult);

                                filteredBusinesses.push(obj);
                            }
                        }
                    }
                }

                return filteredBusinesses;
            } else {
                if (state.geographicBounds) {
                    const filteredBusinesses = [];

                    for (let business of state.businesses) {
                        for (let gameStore of business.stores) {
                            const latLng = L.latLng(parseFloat(gameStore.lat), parseFloat(gameStore.lng));
                            if (state.geographicBounds.contains(latLng)) {
                                const obj = Object.assign(gameStore);
                                obj.distanceToCenterPoint = 1.0;
                                obj.business = business;
                                obj.searchResult = null;

                                filteredBusinesses.push(obj);
                            }
                        }
                    }

                    return filteredBusinesses;
                } else {
                    return state.businesses;
                }
            }
        }
    },
    actions: {
        getBusinesses({commit}) {
            axios.get('shops/')
                .then(response => {
                    commit('setBusinesses', response.data);

                    const idx = lunr(function () {
                        this.ref('id');
                        this.field('name');
                        this.field('businessName');
                        this.field('address1');
                        this.field('city');
                        this.field('zipCode');

                        this.pipeline.remove(lunr.stemmer);
                        this.pipeline.remove(lunr.stopWordFilter);

                        for (let business of response.data) {
                            for (let gameStore of business.stores) {
                                const doc = {
                                    id: gameStore.id,
                                    businessName: business.name,
                                    name: gameStore.name,
                                    address1: gameStore.address1,
                                    city: gameStore.city,
                                    zipCode: gameStore.zipCode
                                };

                                this.add(doc);
                            }
                        }
                    });

                    commit('setSearchIndex', idx);
                })
                .catch(error => {
                    console.log(error);
                });
        },
        getTags({commit}) {
            commit('setIsLoadingTags', true);

            axios.get('tags/')
                .then(response => {
                    commit('setTags', response.data);
                    commit('setIsLoadingTags', false);
                });
        },
        search({commit, state}, searchString) {
            if (state.searchIndex) {
                commit('setSearchResults', state.searchIndex.search(searchString.trim() + '*'));
                commit('setSearchText', searchString.trim());
            }
        },
        setGeographicBounds({commit}, geographicBounds) {
            commit('setGeographicBounds', geographicBounds);
        }
    },
    mutations: {
        setIsLoadingTags(state, isLoadingTags) {
            state.isLoadingTags = isLoadingTags;
        },
        setSearchIndex(state, idx) {
            state.searchIndex = idx;
        },
        setSearchResults(state, results) {
            state.searchResults = results;
        },
        setBusinesses(state, payload) {
            state.businesses = payload;
        },
        setGeographicBounds(state, payload) {
            state.geographicBounds = payload;
        },
        setSearchText(state, payload) {
            state.searchText = payload;
        },
        setTags(state, payload) {
            state.tags = payload;
        }
    }
};
