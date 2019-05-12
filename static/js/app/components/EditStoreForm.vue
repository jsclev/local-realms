<template>
<!--    v-show="selectedGameStore && isEditingStore"-->
    <form
          id="edit-store-form"
          autocomplete="off">
        <div class="mdc-text-field mdc-text-field--outlined">
            <input class="mdc-text-field__input">
            <div class="mdc-notched-outline">
                <div class="mdc-notched-outline__leading"></div>
                <div class="mdc-notched-outline__notch">
                    <label class="mdc-floating-label">Name</label>
                </div>
                <div class="mdc-notched-outline__trailing"></div>
            </div>
        </div>
        <label for="edit-store-name">Name</label>
        <input id="edit-store-name" class="input-common" type="text" v-model="storeName"/>
        <label for="edit-store-website">Website</label>
        <input id="edit-store-website" class="input-common" type="text" v-model="website"/>
        <label for="edit-store-facebook">Facebook</label>
        <input id="edit-store-facebook" class="input-common" type="text" v-model="facebook"/>
        <label for="edit-store-phone">Phone</label>
        <input id="edit-store-phone" class="input-common" type="text" v-model="phone"/>
    </form>
</template>

<script>
    import store from '../store/index';
    import {MDCTextField} from '@material/textfield';


    export default {
        mounted: function () {
            $('#edit').click(function () {
                console.log('sasd');
                $('#edit').addClass('open');
            });

            const textField = new MDCTextField(document.querySelector('.mdc-text-field'));

        },
        computed: {
            facebook: {
                get() {
                    if (this.selectedGameStore) {
                        return store.state.selectedGameStore.business.facebook;
                    }

                    return '';
                },
                set() {

                }
            },
            isEditingStore() {
                return store.state.isEditingStore;
            },
            phone: {
                get() {
                    if (this.selectedGameStore) {
                        return store.state.selectedGameStore.phone;
                    }

                    return '';
                },
                set() {

                }
            },
            storeName: {
                get() {
                    if (this.selectedGameStore) {
                        return store.state.selectedGameStore.business.name;
                    }

                    return '';
                },
                set() {

                }
            },
            selectedGameStore() {
                return store.state.selectedGameStore;
            },
            website: {
                get() {
                    if (this.selectedGameStore) {
                        return store.state.selectedGameStore.business.website;
                    }

                    return '';
                },
                set() {

                }
            },
        }
    }
</script>

<style scoped>

    #edit-store-form {
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
