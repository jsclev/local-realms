import Vue from 'vue'
import Vuex from 'vuex'
import businessList from './modules/BusinessList.js'

Vue.use(Vuex);
Vue.config.productionTip = false;

export default new Vuex.Store({
    namespaced: true,
    state: {
        isEditingStore: false,
        isCreatingNewStore: false,
        selectedGameStore: null
    },
    modules: {
        businessList: businessList
    },
    actions: {
        setIsEditingStore({commit}, payload) {
            commit('setIsEditingStore', payload);
        },
        setIsCreatingNewStore({commit}, payload) {
            commit('setIsCreatingNewStore', payload);
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
        setIsCreatingNewStore(state, payload) {
            state.isCreatingNewStore = payload;
        },
        setSelectedGameStore(state, payload) {
            state.selectedGameStore = payload;
        }
    }
});
