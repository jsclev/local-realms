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
                searchResults = state.searchIndex.search(searchString);
            }

            const filteredBusinesses = [];
            for (let searchResult of searchResults) {
                for (let business of state.businesses) {
                    if (parseInt(searchResult.ref) === business.id) {
                        filteredBusinesses.push(business);
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

                    for (let gameStore of businesses) {
                        this.add(gameStore);
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
