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
        setSelectedGameStore({commit}, payload) {
            commit('setSelectedGameStore', payload);
        }
    },
    mutations: {
        setSelectedGameStore(state, payload) {
            state.selectedGameStore = payload;
        }
    }
});
