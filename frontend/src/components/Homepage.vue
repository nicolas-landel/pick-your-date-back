<template>
  <div class="hello">
    JJJJ
  </div>
</template>

<script>
import api from "@/setup/api";

export default {
  name: "Homepage",
  async setup() {
    console.log("NETERRRR", api);
    const res = await api.get("/place/");
    const places = res.data
    console.log("PLACESSSS", places, res);
  }
};
</script>

<style scoped>

</style>
