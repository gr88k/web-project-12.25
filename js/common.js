function formatNumber(num) {
    if (num === undefined || num === null) return 'N/A';
    return num.toString();
}

function formatArea(area) {
    if (area === undefined || area === null) return 'N/A';
    return area + ' km²';
}

function formatPopulation(population) {
    if (population === undefined || population === null) return 'N/A';
    return population.toString();
}

function getUrlParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

function showError(containerId, message, showRetry = false) {
    const container = document.getElementById(containerId);
    if (!container) return;
    
    let html = `<div class="error">${message}</div>`;
    if (showRetry) {
        html += `<button class="btn" onclick="window.location.reload()">Retry</button>`;
    }
    container.innerHTML = html;
}

function showLoading(containerId, message = 'Loading...') {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = `<div class="loading">${message}</div>`;
}

async function fetchData(url, options = {}) {
    try {
        const response = await fetch(url, options);
        if (!response.ok) throw new Error('HTTP ' + response.status);
        return await response.json();
    } catch (error) {
        console.error('Fetch error:', error);
        throw error;
    }
}

function createTagsList(items) {
    if (!items || items.length === 0) {
        return '<span style="color: #94a3b8;">No data</span>';
    }
    
    return items.map(item => `<span class="tag">${item}</span>`).join('');
}