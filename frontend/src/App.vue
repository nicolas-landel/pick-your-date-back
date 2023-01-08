<template>
  <VApp id="app">
    <AppNavbar/>
    <!-- <Suspense> -->
      <RouterView />
      <!-- <template #fallback>
        Loading...
      </template> -->
    <!-- </Suspense> -->
  </VApp>
  
</template>

<script setup>
import AppNavbar from "@/components/shared/AppNavbar.vue"

</script>

<style scoped>

</style>
