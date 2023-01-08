<template>
  <div>
    <h3>{{ $t("Login")}}</h3>
    <VForm>
      <VTextField
        v-model="loginEmail"
        name="email"
        :label="$t('Email')"
        type="text"
        required
      ></VTextField>
      <VTextField
        v-model="loginPassword"
        name="password"
        :label="$t('Password')"
        type="password"
        required
      ></VTextField>
      <VBtn class="mt-4" color="primary" @click="submitLogin"> {{ $t('Login')}} </VBtn>
    </VForm>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "@/setup/api";
import router from "@/router"
defineProps({});

const loginEmail = ref("");
const loginPassword = ref("");

const submitLogin = async () => {
  console.log("HHHHHHH", loginEmail.value, loginPassword.value);
  const response = await api.post("/user/login/", {
    email: loginEmail.value,
    password: loginPassword.value,
  });
  console.log("REPPPP", response);
  if (response && response.status === 202) {
    console.log("PUSHHH")
    router.push({ name: 'dashboard'})
  }
};
</script>

<style scoped>
</style>