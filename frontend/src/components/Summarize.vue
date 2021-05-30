<template>
    <div class="container">
        <LoadingSpinner class="spinner" v-if="loading" />
        <p v-else class="summary">{{ summary }}</p>
        <div class="buttons">
            <ImageButton @click="refreshSummary()" imgName="retry.png" title="Retry" />
            <ImageButton @click="$emit('returnHome')" imgName="exit.png" title="Back" />
        </div>
    </div>
</template>
<script>
import { getCurrentVideoId, generateSummary } from '../lib';
import ImageButton from './ImageButton';
import LoadingSpinner from './LoadingSpinner';

export default {
    name: 'Summarize',
    components: {
        ImageButton,
        LoadingSpinner
    },
    data() {
        return {
            summary: '',
            loading: false
        }
    },
    async mounted() {
        this.refreshSummary();
    },
    methods: {
        async refreshSummary() {
            this.loading = true;

            const videoId = await getCurrentVideoId();
            const summary = await generateSummary(videoId);

            this.summary = summary;
            this.loading = false;
        }
    }
}
</script>
<style scoped>
    .spinner {
        margin-left: auto;
        margin-right: auto;
    }

    .container {
        display: flex;
        flex-direction: column;
        justify-content: space-evenly;
        height: 100%;
        overflow: auto;
    }

    .buttons {
        display: flex;
        align-items: center;
        justify-content: space-evenly;
    }
</style>