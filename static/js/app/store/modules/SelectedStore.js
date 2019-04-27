export default {
    namespaced: true,
    state: {
        gameStore: null
    },
    actions: {
        select({commit}, gameStore) {
            commit('setSelection', gameStore);
        }
    },
    mutations: {
        setSelection(state, gameStore) {
            state.gameStore = gameStore;
        }
    }
};
