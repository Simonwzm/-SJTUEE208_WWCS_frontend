<template>
  <div id="app">
    <NavBar />
    <leftSideBar />
    <router-view/>
  </div>
</template>

<style lang="scss">
#app {
  height: 100vh;
  width: 100%;
}
</style>

<script>
export default 
{
  name: 'App',
  components: 
  {
    NavBar: () => import('@/components/NavBar.vue'),
    leftSideBar: () => import('@/components/LeftSideBar.vue'),
  }
}


</script>
