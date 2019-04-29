import businessList from './modules/BusinessList.js'

export default new Vuex.Store({
    namespaced: true,
    state: {
        selectedGameStore: null
    },
    modules: {
        businessList: businessList
    },
    actions: {
        setSelectedGameStore({commit, state}, payload) {
            if (state.selectedGameStore && state.selectedGameStore.id === payload.id) {
                commit('setSelectedGameStore', null);
            }
            else {
                commit('setSelectedGameStore', payload);
            }
        }
    },
    mutations: {
        setSelectedGameStore(state, payload) {
            state.selectedGameStore = payload;
        }
    }
});
