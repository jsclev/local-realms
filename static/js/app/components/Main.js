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
            </div>
            <Menu></Menu>
        </div>`
});
