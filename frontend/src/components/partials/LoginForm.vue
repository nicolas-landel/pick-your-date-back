<template>
  <div>
    <h3>{{ $t("Login")}}</h3>
    <VForm>
      <VTextField
        v-model="loginEmail"
        name="email"
        label="Email"
        type="text"
        required
      ></VTextField>
      <VTextField
        v-model="loginPassword"
        name="password"
        :label="$t('password')"
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
defineProps({});

const loginEmail = ref("");
const loginPassword = ref("");

const submitLogin = async () => {
  console.log("HHHHHHH", loginEmail.value, loginPassword.value);
  const loginResponse = await api.post("/user/login/", {
    email: loginEmail.value,
    password: loginPassword.value,
  });
  console.log("REPPPP", loginResponse);
};
</script>

<style scoped>
</style>