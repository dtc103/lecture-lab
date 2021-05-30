const MOCK = false;

const VIDEO_REGEX = /^https:\/\/www.youtube.com\/watch\?v=([^?&#]+)/;

async function getCurrentPage() {
    return new Promise(resolve => {
        if (MOCK) {
            resolve('https://www.youtube.com/watch?v=NhZJjQ9f17E');
        }

        chrome.tabs.query({ active: true, lastFocusedWindow: true }, tabs => {
            resolve(tabs[0].url);
        });
    });
}

export async function isOnVideoPage() {
    const page = await getCurrentPage();
    return page.match(VIDEO_REGEX);
}

async function sleep(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}

export async function generateSummary(videoId) {
    if (MOCK) {
        await sleep(1000);
        return 'asdasdsadddddddd ddddddd dddddddd dddddddddddd dddddddddddddddddd ddddddd ddddddddddd asdasdsadddddddd ddddddd dddddddd dddddddddddd dddddddddddddddddd ddddddd ddddddddddd asdasdsadddddddd ddddddd dddddddd dddddddddddd dddddddddddddddddd ddddddd ddddddddddd asdasdsadddddddd ddddddd dddddddd dddddddddddd dddddddddddddddddd ddddddd ddddddddddd '
    }
    const resp = await fetch(`http://localhost:8000/summarize?video_id=${videoId}`)
    const { message } = await resp.json()

    return message;
}

export async function generateQuestionAnswerPairs(videoId) {
    if (MOCK) {
        await sleep(1000);
        return [
            {
                question: 'Who is the impostor?',
                answer: 'sus'
            },
            {
                question: 'amogus',
                answer: 'sugoma'
            }
        ]
    }

    const resp = await fetch(`http://localhost:8000/flashcards?video_id=${videoId}`)
    const { message } = await resp.json()

    return JSON.parse(message);
}

export async function generateAnswer(videoId, question) {
    if (MOCK) {
        await sleep(1000);
        return Math.random()
    }

    const resp = await fetch('http://localhost:8000/questions?' + new URLSearchParams({
        video_id: videoId,
        question
    }));
    const { message } = await resp.json();

    return message;
}

export async function getCurrentVideoId() {
    if (!await isOnVideoPage()) {
        return false;
    }

    const currLink = await getCurrentPage();

    return VIDEO_REGEX.exec(currLink)[1];
}