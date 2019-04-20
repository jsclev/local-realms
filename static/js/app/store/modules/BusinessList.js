export default {
    namespaced: true,
    state: {
        businesses: [],
        searchIndex: null,
        searchResults: []
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
                        if (parseInt(searchResult.ref) === gameStore.i) {
                            filteredBusinesses.push(business);
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
                    this.ref('i.py');
                    this.field('name');
                    this.field('businessName');
                    this.field('street1');
                    this.field('city');
                    this.field('zipCode');

                    this.pipeline.remove(lunr.stemmer);
                    this.searchPipeline.remove(lunr.stemmer);

                    for (let business of businesses) {
                        for (let gameStore of business.stores) {
                            const doc = {
                                id: gameStore.i,
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
