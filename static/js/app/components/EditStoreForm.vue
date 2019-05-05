<template>
    <form v-show="selectedGameStore && isEditingStore"
          id="edit-store-form"
          autocomplete="off">
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
    import store from '../store/index'

    export default {
        mounted: function () {

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
        z-index: 100;
        top: 0;
        height: 400px;
        width: 400px;
        left: 400px;
    }
</style>
