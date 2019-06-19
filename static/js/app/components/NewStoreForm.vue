<template>
    <form v-show="isCreatingNewStore"
          class="open"
          id="new-store-form"
          autocomplete="off">
        <label for="name">Name</label>
        <input id="name" class="input-common" type="text"/>
        <br>
        <label for="website">Website</label>
        <input id="website" class="input-common" type="text"/>
        <br>
        <label for="facebook">Facebook</label>
        <input id="facebook" class="input-common" type="text"/>
        <br>
        <label for="phone">Phone</label>
        <input id="phone" class="input-common" type="text"/>
        <br>
        <label for="email">Email</label>
        <input id="email" class="input-common" type="text"/>
        <br>
        <label for="address">Address</label>
        <input id="address" class="input-common" type="text"/>
        <br>
        <label for="city">City</label>
        <input id="city" class="input-common" type="text"/>
        <br>
        <label for="state">State</label>
        <input id="state" class="input-common" type="text"/>
        <br>
        <input type="submit" class="input-common"/>
    </form>
</template>

<script>
        import store from '../store/index';
    // import {MDCTextField} from '@material/textfield';

    export default {
        computed: {
            isCreatingNewStore() {
                return store.state.isCreatingNewStore;
            },
        }
    }

</script>

<style scoped>
    #new-store-form {
        position: absolute;
        z-index: 2;
        top: 0;
        height: 100%;
        width: 380px;
        left: -4000px;
        background-color: white;
        padding: 10px;
        -webkit-transition: all 250ms;
        -moz-transition: all 250ms;
        -ms-transition: all 250ms;
        -o-transition: all 250ms;
        transition: all 250ms;
    }

    .open {
        left: 0 !important;
    }

</style>