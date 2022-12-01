<template>
<div style="width:100vw; height:100vh;z-index:10;">
    <PicContainer />
</div>  
</template>

<script>

export default {
    name: 'Playground',
    components: {
        PicContainer: () => import('@/components/PicContainer.vue'),

    }
}
</script>

<style>

</style>