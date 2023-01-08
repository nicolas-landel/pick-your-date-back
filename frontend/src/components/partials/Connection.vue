<template>
  <div>
    <div class="homepage-grid">
      <LoginForm />
      <div class="homepage-separator"></div>
      <SignupForm />
    </div>
  </div>
</template>

<script setup>
import LoginForm from "@/components/partials/LoginForm.vue";
import SignupForm from "@/components/partials/SignupForm.vue";
defineProps({});
</script>

<style scoped>
.homepage-grid {
  display: grid;
  grid-template-columns: 45% 1px 45%;
  margin-left: 10%;
  margin-right: 10%;
  grid-column-gap: 50px;
}

.homepage-separator {
  border-left: outset;
  padding-top: 40px;
}
</style>