export default {
    namespaced: true,
    state: {
        businesses: [],
        searchIndex: null,
        searchResults: [],
        centerLocation: {
            lat: 37.774691,
            lng: -77.697109

        }
    },
    actions: {
        search({commit, state}, searchString) {
            let searchResults = [];

            if (state.searchIndex) {
                searchResults = state.searchIndex.search(searchString.trim() + '*');
            }

            const filteredBusinesses = [];
            for (let searchResult of searchResults) {
                for (let business of state.businesses) {
                    for (let gameStore of business.stores) {
                        if (parseInt(searchResult.ref) === gameStore.id) {
                            const obj = Object.assign(gameStore);
                            obj.distanceToCenterPoint = 1.0;
                            obj.business = business;
                            obj.searchResult = Object.assign(searchResult);

                            filteredBusinesses.push(obj);
                        }
                    }
                }
            }
            commit('setSearchResults', filteredBusinesses);
        },
        getBusinesses({commit}) {
            $.get('shops/', function (businesses, status) {
                commit('setBusinesses', businesses);

                const idx = lunr(function () {
                    this.ref('id');
                    this.field('name');
                    this.field('businessName');
                    this.field('street1');
                    this.field('city');
                    this.field('zipCode');

                    this.pipeline.remove(lunr.stemmer);
                    this.pipeline.remove(lunr.stopWordFilter);

                    for (let business of businesses) {
                        for (let gameStore of business.stores) {
                            const doc = {
                                id: gameStore.id,
                                businessName: business.name,
                                name: gameStore.name,
                                street1: gameStore.street1,
                                city: gameStore.city,
                                zipCode: gameStore.zipCode
                            };

                            this.add(doc);
                        }
                    }
                });

                commit('setSearchIndex', idx);
            });
        }
    },
    mutations: {
        setSearchIndex(state, idx) {
            state.searchIndex = idx;
        },
        setSearchResults(state, results) {
            state.searchResults = results;
        },
        setBusinesses(state, payload) {
            state.businesses = payload;
        }
    }
};
