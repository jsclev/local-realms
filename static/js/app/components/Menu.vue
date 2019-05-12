<template>
    <div id="menu">
        <div class="header">
            <div id="menu-back-icon" class="icon"></div>
        </div>
        <div id="menu-content">
            <a id="about-link" class="menu-item" href="about/">About Us</a>
            <a id="contact-link" class="menu-item" href="contact/">Contact Us</a>
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
    #menu {
        width: 350px;
        height: 100%;
        position: absolute;
        z-index: 1000;
        background-color: white;
        transition: ease 250ms;
        left: -350px;
        display: flex;
        flex-direction: column;
    }

    .menu-open {
        left: 0 !important;
    }

    .menu-item {
        color: black;
        -webkit-transition: ease 250ms;
        -moz-transition: ease 250ms;
        -ms-transition: ease 250ms;
        -o-transition: ease 250ms;
        padding: 6px 10px;

    }

    #about-link {
    }

    #contact-link {

    }

</style>
