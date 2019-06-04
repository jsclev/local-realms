<template>
    <div id="menu">
        <div class="header">
            <div id="menu-back-icon" class="icon"></div>
            <div id="title">Local Realms</div>
        </div>
        <div id="menu-content">
            <a id="about-link" class="menu-item" href="about/">
                <i class="material-icons icons">info_outline</i>
                About Us
            </a>
            <a id="contact-link" class="menu-item" href="contact/">
                <i class="material-icons icons" style="margin-top: 1px">chat_bubble_outline</i>
                Contact Us
            </a>
        </div>
    </div>
</template>

<script>
    export default {
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
    }
</script>

<style scoped>
    .header {
        padding: 10px;
        border-bottom: #e4e4e4 1px solid;
        margin-bottom: 10px;
        display: flex;
        align-content: center;
    }
    
    #title {
        color: #8f8f8f;
        font-size: 25px;
        display: flex;
        align-items: center;
        margin-left: 15px;
        margin-bottom: 3px;
    }

    #menu {
        width: 300px;
        height: 100%;
        position: absolute;
        z-index: 1000;
        background-color: white;
        transition: ease 250ms;
        left: -300px;
        display: flex;
        flex-direction: column;
    }

    .menu-open {
        left: 0 !important;
    }

    .menu-item {
        color: black;
        -webkit-transition: ease 50ms;
        -moz-transition: ease 50ms;
        -ms-transition: ease 50ms;
        -o-transition: ease 50ms;
        padding-left: 24px;
        margin-right: 8px;
        border-radius: 0 30px 30px 0;
        height: 40px;
        font-size: 14px;
        display: flex;
        align-items: center;
    }

    .menu-item:hover {
        background-color: rgba(0, 66, 255, 0.05);
    }

    #menu-content {
        display: flex;
        flex-direction: column;
    }
    .material-icons.icons {
        color: rgba(0, 0, 0, 0.5);
        margin-right: 15px;
    }

    #about-link {
    }

    #contact-link {

    }

</style>
