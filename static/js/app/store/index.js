import businessList from './modules/BusinessList.js'
import selectedStore from './modules/SelectedStore.js'

export default new Vuex.Store({

    modules: {
        businessList: businessList,
        selectedStore: selectedStore
    }
});
