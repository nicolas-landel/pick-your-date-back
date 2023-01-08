<template>
    <VContainer class="fill-height">
      <VResponsive class="d-flex align-center text-center fill-height">
        <!-- TODO set condition on user -->
        <Connection/>
        <VBtn @click="goDashboard">Go to Dashboard</VBtn>
      </VResponsive>
    </VContainer>
</template>

<script setup>
import { ref } from "vue";
import AppNavbar from "@/components/shared/AppNavbar.vue";
import Connection from "@/components/partials/Connection.vue";
import { useRouter, useRoute } from 'vue-router'

defineProps({});

const user = ref(false);
const router = useRouter()

const goDashboard = () => {
  router.push("/dashboard")
}

</script>

<style scoped>
</style>
