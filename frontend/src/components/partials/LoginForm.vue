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
      <VBtn 
        class="mt-4"
        color="primary"
        :loading="loginLoading"
        @click="submitLogin"
      > {{ $t('Login')}} </VBtn>
    </VForm>
  </div>
</template>

<script setup>
import { ref } from "vue";
import api from "@/setup/api";
import { useRouter } from 'vue-router';
import { TokenService } from "@/setup/tokenService"
defineProps({});

const loginEmail = ref("");
const loginPassword = ref("");
const loginLoading = ref(false)
const router = useRouter()

const submitLogin = async () => {
  loginLoading.value = true
  try {
    const response = await api.post("/user/login/", {
      email: loginEmail.value,
      password: loginPassword.value,
    });
    if (response && response.status === 202) {
      loginLoading.value = false
      const token = response.data.token
      console.log("REPP", response, token)
      TokenService.saveToken(token)
      router.push({ name: 'dashboard'})
    }
  } catch(e) {
    console.error(e)
  }
  
};
</script>

<style scoped>
</style>