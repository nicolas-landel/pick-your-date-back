<template>
  <VApp id="app">
    <AppNavbar />
    <RouterView class="app-content"/>
  </VApp>
</template>

<script setup>
import AppNavbar from "@/components/shared/AppNavbar.vue";
</script>

<style scoped>
.app-content {
  height: calc(100% - 50px);
  margin-top: 50px;
}
</style>
