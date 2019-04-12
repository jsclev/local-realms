export default {
    namespaced: true,
    state: {
        stores: [],
        searchIndex: null,
        searchResults: []
    },
    actions: {
        search({commit, state}, searchString) {
            let searchResults = [];

            if (state.searchIndex) {
                searchResults = state.searchIndex.search(searchString);
            }

            const filteredStores = [];
            for (let searchResult of searchResults) {
                for (let gameStore of state.stores) {
                    if (parseInt(searchResult.ref) === gameStore.id) {
                        filteredStores.push(gameStore);
                    }
                }
            }
            commit('setSearchResults', filteredStores);
        },
        getStores({commit}) {
            $.get('shops/', function (stores, status) {
                commit('setStores', stores);

                const idx = lunr(function () {
                    this.ref('id');
                    this.field('name');

                    for (let gameStore of stores) {
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
        setStores(state, payload) {
            state.stores = payload;
        }
    }
};
