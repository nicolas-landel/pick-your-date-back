<template>
  <VAppBar dense elevation="2" app flat dark height="50">
    <VIcon class="ml-10">mdi-calendar</VIcon>
    <VToolbarTitle>Pick Your Date</VToolbarTitle>
    <RouterLink to="/"  >Connection</RouterLink>
    <RouterLink to="/dashboard"  >Dashboard</RouterLink>
  </VAppBar>
</template>

<script setup>
defineProps({});
</script>

<style>
</style>