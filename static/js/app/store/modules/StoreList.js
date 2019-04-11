export default {
    namespaced: true,
    state: {
        stores: []
    },
    actions: {
        getStores({commit}) {
            $.get('shops/', function (data, status) {
                commit('setStores', data);

            });
        }
    },
    mutations: {
        setStores(state, payload) {
            state.stores = payload;
        }
    }
};
