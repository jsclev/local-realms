import Vue from 'vue'
import Filters from './components/Filters.vue'
import MapContainer from './components/Map.vue'
import Menu from './components/Menu.vue'
import SearchBox from './components/SearchBox.vue'
import SelectedGameStore from './components/SelectedGameStore.vue'
import StoreList from './components/StoreList.vue'

new Vue({
    el: '#app',
    components: {
        Filters,
        MapContainer,
        Menu,
        SearchBox,
        SelectedGameStore,
        StoreList
    },
    template: `
        <div>
            <div id="menu-dim"></div>
            <div id="main-panel">
                <SearchBox></SearchBox>
                <Filters></Filters>
                <div id="filter-dim"></div>
                <StoreList></StoreList>
                <MapContainer></MapContainer>
                <SelectedGameStore></SelectedGameStore>
            </div>
            <Menu></Menu>
        </div>`
});
