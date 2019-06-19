<template>
    <form v-show="isCreatingNewStore"
          class="open"
          id="new-store-form"
          autocomplete="off"
          method="post"
          action="add_store/">
        <input type="hidden" name="csrfmiddlewaretoken" v-bind:value=csrfToken />
        <label for="name">Name</label>
        <input id="name" name="name" required class="input-common" type="text"/>
        <br>
        <label for="website">Website</label>
        <input id="website" name="website" class="input-common" type="text"/>
        <br>
        <label for="facebook">Facebook</label>
        <input id="facebook" name="facebook" class="input-common" type="text"/>
        <br>
        <label for="phone">Phone</label>
        <input id="phone" name="phone" class="input-common" type="text"/>
        <br>
        <label for="email">Email</label>
        <input id="email" name="email" class="input-common" type="email"/>
        <br>
        <label for="address">Address</label>
        <input id="address" name="address" required class="input-common" type="text"/>
        <br>
        <label for="address-line-2">Address Line 2</label>
        <input id="address-line-2" name="address-line-2" class="input-common" type="text"/>
        <br>
        <label for="city">City</label>
        <input id="city" name="city" required class="input-common" type="text"/>
        <br>
        <label for="state">State</label>
        <input id="state" name="state" required class="input-common" type="text"/>
        <br>
        <label for="zip-code">Zip Code</label>
        <input id="zip-code" name="zip-code" required class="input-common" type="number"/>
        <br>
        <label for="latitude">Latitude</label>
        <input id="latitude" name="latitude" required class="input-common" type="text"/>
        <br>
        <label for="longitude">Longitude</label>
        <input id="longitude" name="longitude" required class="input-common" type="text"/>
        <br>
        <br>
        <input type="submit" class="input-common"/>
        <br>
        <br>
        <a @click="cancel" href="#">Cancel</a>
    </form>
</template>

<script>
        import store from '../store/index';
    // import {MDCTextField} from '@material/textfield';

    export default {
        data: function () {
            return {
                csrfToken : this.getCookie('csrftoken')
            }
        },
        computed: {
            isCreatingNewStore() {
                return store.state.isCreatingNewStore;
            },
        },

        methods: {
            cancel(){
                store.dispatch("setIsCreatingNewStore", false);
            },
            getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
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