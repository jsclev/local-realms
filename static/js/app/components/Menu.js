Vue.component('Menu', {
    template: `
         <div id="menu">
            <div class="header">
                <div id="menu-back-icon" class="icon"></div>
            </div>
        </div>`,
    mounted: function () {
        $('.menu-icon').click(function () {
            $('#menu').addClass('menu-open');
            $('#map').addClass('dim');
            $('#store-list').addClass('dim');
            $('.search-outer').addClass('dim');
            $('#menu-back-icon').addClass('back-icon');
            $('.tag-filter').addClass('dim')
        });

        $('#menu-back-icon').click(function () {
            $('#menu').removeClass('menu-open');
            $('#map').removeClass('dim');
            $('#store-list').removeClass('dim');
            $('.search-outer').removeClass('dim');
            $('#menu-back-icon').removeClass('back-icon');
            $('.tag-filter').removeClass('dim')
        });
    }
});
