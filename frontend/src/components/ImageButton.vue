<template>
    <div class="container">
        <img :src="require(`@/assets/${imgName}`)" />
        <span>{{ title }}</span>
    </div>
</template>

<script>
export default {
    name: 'ImageButton',
    props: {
        imgName: String,
        title: String
    }
}
</script>

<style scoped>
    .container {
        transition: all 0.1s;
        display: inline-flex;
        flex-direction: column;
        align-items: center;
        cursor: pointer;
    }

    .container:hover {
        transform: translateY(-2.5px);
    }

    img {
        width: 30px;
    }
</style>