new Vue({
    el: '#main-vue-hook',
    template: `
        <div>
            <div id="menu-dim"></div>
            <div id="main-panel">
                <SearchBox></SearchBox>
                <Filters></Filters>
                <StoreList></StoreList>
                <Map></Map>
                <SelectedGameStore></SelectedGameStore>
            </div>
            <Menu></Menu>
        </div>`
});
