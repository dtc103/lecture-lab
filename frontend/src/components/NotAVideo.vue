<template>
    <h1>Navigate to a youtube video to use me!</h1>
    <button @click="$emit('returnHome')">Test</button>
</template>
<script>
export default {
    name: 'NotAVideo'
};
</script>
