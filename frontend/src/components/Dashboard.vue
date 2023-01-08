<template>
  <h1>{{ $t("Dashboard") }}</h1>
</template>

<script setup>
import { ref } from "vue";
import api from "@/setup/api";

const response = await api.get("/place/")
console.log("RESPONSEEEE", response)
</script>

<style scoped>
</style>