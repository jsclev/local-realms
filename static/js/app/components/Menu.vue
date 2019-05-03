import Vue from 'vue'

export default Vue.component('Menu', {
    template: `
         <div id="menu">
            <div class="header">
                <div id="menu-back-icon" class="icon"></div>
            </div>
        </div>`,
    mounted: function () {
        $('.menu-icon').click(function () {
            $('#menu').addClass('menu-open');
            $('#menu-back-icon').addClass('back-icon');
            $('#menu-dim').addClass('dimmed');
        });

        $('#menu-back-icon').click(function () {
            $('#menu').removeClass('menu-open');
            $('#menu-back-icon').removeClass('back-icon');
            $('#menu-dim').removeClass('dimmed');
        });
        $('#menu-dim').click(function () {
            $('#menu').removeClass('menu-open');
            $('#menu-back-icon').removeClass('back-icon');
            $('#menu-dim').removeClass('dimmed');
        })
    }
});
