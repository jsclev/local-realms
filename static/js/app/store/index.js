import Vue from 'vue'
import Vuex from 'vuex'
import businessList from './modules/BusinessList.js'

Vue.use(Vuex);
Vue.config.productionTip = false;

export default new Vuex.Store({
    namespaced: true,
    state: {
        isEditingStore: false,
        selectedGameStore: null
    },
    modules: {
        businessList: businessList
    },
    actions: {
        setIsEditingStore({commit}, payload) {
            commit('setIsEditingStore', payload);
        },
        setSelectedGameStore({commit, state}, payload) {
            if (state.selectedGameStore && state.selectedGameStore.id === payload.id) {
                commit('setSelectedGameStore', null);
            }
            else {
                commit('setSelectedGameStore', payload);
            }

            commit('setIsEditingStore', false);
        }
    },
    mutations: {
        setIsEditingStore(state, payload) {
            state.isEditingStore = payload;
        },
        setSelectedGameStore(state, payload) {
            state.selectedGameStore = payload;
        }
    }
});
