function getReadableTime(seconds) {
    let timeString = "";

    if (seconds < 0) {
        throw new Error("Input value must be non-negative");
    }

    if (seconds < 60) {
        timeString = `${Math.round(seconds)}s`;
    } else {
        let minutes = Math.floor(seconds / 60);
        seconds %= 60;
        let hours = Math.floor(minutes / 60);
        minutes %= 60;
        let days = Math.floor(hours / 24);
        hours %= 24;

        if (days > 0) {
            timeString += `${Math.round(days)}days, `;
        }
        if (hours > 0) {
            timeString += `${Math.round(hours)}h:`;
        }
        timeString += `${Math.round(minutes)}m:${Math.round(seconds).toString().padStart(2, '0')}s`;
    }

    return timeString;
}

