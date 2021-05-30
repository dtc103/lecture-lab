<template>
    <div class="container">
        <input v-model="question" type="text" placeholder="Enter a question about the video here...">
        <LoadingSpinner class="spinner" v-if="loading" />
        <p v-else>{{ answer }}</p>
        <div class="buttons">
            <ImageButton @click="answerQuestion()" imgName="ask.png" title="Ask" />
            <ImageButton @click="$emit('returnHome')" imgName="exit.png" title="Back" />
        </div>
    </div>
</template>
<script>
import { getCurrentVideoId, generateAnswer } from '../lib';
import ImageButton from './ImageButton';
import LoadingSpinner from './LoadingSpinner';

export default {
    name: 'Ask',
    components: {
        ImageButton,
        LoadingSpinner
    },
    data() {
        return {
            question: '',
            answer: '',
            loading: false
        };
    },
    methods: {
        async answerQuestion() {
            console.log(this.answer, this.question)
            this.loading = true;

            const videoId = await getCurrentVideoId();
            const answer = await generateAnswer(videoId, this.question);

            this.loading = false;
            this.answer = answer;
        }
    }
}
</script>
<style scoped>
    .spinner {
        margin-left: auto;
        margin-right: auto;
    }

    input[type=text] {
        text-align: center;
        width: 70%;
        margin-left: auto;
        margin-right: auto;
        border: none;
        border-bottom: 1.5px dashed black;
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