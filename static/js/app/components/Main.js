new Vue({
    el: '#main-vue-hook',
    template: `
        <div id="main-panel">
            <Menu></Menu>
            <SearchBox></SearchBox>
            <Filters></Filters>
            <StoreList></StoreList>
            <Map></Map>
            <SelectedGameStore></SelectedGameStore>
        </div>`
});
