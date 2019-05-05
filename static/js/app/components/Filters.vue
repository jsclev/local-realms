<template>
    <div id="filters">
        <div v-for="tag in tags" class="tag-filter checked" :id="tag.name">
            <button class="filter-item">{{ tag.name }}</button>
            <div class="check-mark check-icon-show"></div>
        </div>
        <div class="content">
            <div class="number-filters">0 filters</div>
            <button class="cancel" ripple="ripple">CANCEL</button>
            <button class="apply" ripple="ripple">APPLY</button>
        </div>
    </div>
</template>

<script>
    import store from '../store/index'

    export default {
        data: function () {
            return {
                errors: [],
                selectedTagIds: []
            }
        },
        mounted: function () {
            store.dispatch('businessList/getTags', null, {root: true});

            const searchContainer = $("#input-container");
            const list = $(".entity-list");
            const searchOuter = $(".search-outer");

            $(document).ready(function () {
                $('.tag-filter').click(function () {
                    $('#save-changes').addClass('save-changes-allowed');
                    var currentID = this.id;
                    currentID = $('[id="' + currentID + '"]');
                    if ($(currentID).hasClass('checked')) {
                        $(currentID).removeClass('checked');
                        $(currentID).children('div').removeClass('check-icon-show');
                        $(currentID).children('button').css('color', 'rgba(0,0,0,.56)')
                    } else {
                        $(currentID).addClass('checked');
                        $(currentID).children('div').addClass('check-icon-show');
                        $(currentID).children('button').css('color', 'rgba(0,0,0,.7)')
                    }
                });
            });

            $('#filter-search').click(function () {
                if ($('#filters').hasClass('filter-expanded')) {
                    $('#filters').removeClass('filter-expanded');
                    list.removeClass("entity-list-transition-filter");
                    searchContainer.removeClass("input-common-filter");
                    searchOuter.removeClass("search-outer-after-filter");
                    $('#filter-dim').removeClass('dimmed');
                } else {
                    $('#filters').addClass('filter-expanded');
                    list.addClass("entity-list-transition-filter");
                    searchContainer.addClass("input-common-filter");
                    searchOuter.addClass("search-outer-after-filter");
                    $('#filter-dim').addClass('dimmed');
                }
            });
            $('#filter-dim').click(function () {
                $('#filters').removeClass('filter-expanded');
                list.removeClass("entity-list-transition-filter");
                searchContainer.removeClass("input-common-filter");
                searchOuter.removeClass("search-outer-after-filter");
                $('#filter-dim').removeClass('dimmed');
            });
            $('.cancel').click(function () {
                $('#filters').removeClass('filter-expanded');
                list.removeClass("entity-list-transition-filter");
                searchContainer.removeClass("input-common-filter");
                searchOuter.removeClass("search-outer-after-filter");
                $('#filter-dim').removeClass('dimmed');
            })
            // Ripple effect
            (function () {
                let cleanUp, debounce, i, len, ripple, rippleContainer, ripples, showRipple;

                debounce = function (func, delay) {
                    let inDebounce;
                    inDebounce = undefined;
                    return function () {
                        let args, context;
                        context = this;
                        args = arguments;
                        clearTimeout(inDebounce);
                        return inDebounce = setTimeout(function () {
                            return func.apply(context, args);
                        }, delay);
                    };
                };

                showRipple = function (e) {
                    let pos, ripple, rippler, size, style, x, y;
                    ripple = this;
                    rippler = document.createElement('span');
                    size = ripple.offsetWidth;
                    pos = ripple.getBoundingClientRect();
                    x = e.pageX - pos.left - (size / 2);
                    y = e.pageY - pos.top - (size / 2);
                    style = 'top:' + y + 'px; left: ' + x + 'px; height: ' + size + 'px; width: ' + size + 'px;';
                    ripple.rippleContainer.appendChild(rippler);
                    return rippler.setAttribute('style', style);
                };

                cleanUp = function () {
                    while (this.rippleContainer.firstChild) {
                        this.rippleContainer.removeChild(this.rippleContainer.firstChild);
                    }
                };

                ripples = document.querySelectorAll('[ripple]');

                for (i = 0, len = ripples.length; i < len; i++) {
                    ripple = ripples[i];
                    rippleContainer = document.createElement('div');
                    rippleContainer.className = 'ripple--container';
                    ripple.addEventListener('mousedown', showRipple);
                    ripple.addEventListener('mouseup', debounce(cleanUp, 2000));
                    ripple.rippleContainer = rippleContainer;
                    ripple.appendChild(rippleContainer);
                }
            }());
        },
        computed: {
            tags: function () {
                const tags = store.state.businessList.tags;

                for (let tag of tags) {
                    this.selectedTagIds.push(tag.id);
                }

                return tags;
            }
        }
    }
</script>
