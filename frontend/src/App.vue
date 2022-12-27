<template>
  <div id="app">
    <Suspense>
      <RouterView />
      <template #fallback>
        Loading...
      </template>
    </Suspense>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

