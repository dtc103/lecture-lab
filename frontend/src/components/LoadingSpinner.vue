<template>
    <img src="@/assets/hourglass.png">
</template>

<script>
export default {
    name: 'LoadingSpinner'
}
</script>

<style scoped>
    @keyframes pulse {
        0% {
            opacity: 1;
        }

        50% {
            opacity: 0;
        }

        100% {
            opacity: 1;
        }
    }

    img {
        width: 40px;
        animation: pulse 1s infinite;
    }
</style>