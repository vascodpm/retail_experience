<template>
    <header class="navbar navbar-dark sticky-top">
        <div class="nav navbar pt-2">
            <div class="navbar-brand shadow-none d-flex align-items-center">
                <img class="navbar-logo" src="@/assets/favicon.png" />
                <h2 class="navbar-title mb-0">
                  New retailer experience
                </h2>
            </div>
        </div>
        <div class="shopping-cart" @click="$emit('open-cart')">
            <span v-if="cartItemCount" class="cart-item-count">{{ cartItemCount }}</span>
            <img class="shopping-cart-logo" src="@/assets/shopping-cart-icon.png" alt="Shopping Cart" />
        </div>
    </header>
</template>

<script>
import "../styles/navbar.css"
import "../styles/shoppingcart.css"

export default {
  name: "NavBar",
  props: {
    shoppingCart: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    cartItemCount() {
      return this.shoppingCart.length;
    },
  },
};
</script>
