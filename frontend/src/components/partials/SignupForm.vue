<template>
  <div>
    <h3>{{ $t("Sign up")}}</h3>
    <VForm>
        <VTextField
        v-model="signupFirstName"
        name="firstName"
        :label="$t('firstName')"
        type="text"
        required
      ></VTextField>
      <VTextField
        v-model="signupLastName"
        name="lastName"
        :label="$t('lastName')"
        type="text"
        required
      ></VTextField>
      <VTextField
        v-model="signupEmail"
        name="email"
        label="Email"
        type="text"
        required
      ></VTextField>
      <VTextField
        v-model="signupPassword"
        name="password"
        :label="$t('password')"
        type="password"
        required
      ></VTextField>
      <VBtn class="mt-4" color="primary" @click="submitSignup"> {{ $t('Sign up')}} </VBtn>
    </VForm>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "@/setup/api";
defineProps({});

const signupFirstName = ref("");
const signupLastName = ref("");
const signupEmail = ref("");
const signupPassword = ref("");

const submitSignup = async () => {
  console.log("HHHHHHH", signupFirstName.value, signupLastName.value);
  const response = await api.post("/user/signup/", {
    first_name: signupFirstName.value,
    last_name: signupLastName.value,
    email: signupEmail.value,
    password: signupPassword.value,
  });
  console.log("REPPPP", response);
};
</script>

<style scoped>
</style>