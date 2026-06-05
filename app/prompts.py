def format_answer_from_chunks(chunks_with_scores, query, threshold=0.1):
    if not chunks_with_scores:
        return "Sorry, I found no relevant movies."
    relevant = [(t, m, s) for t, m, s in chunks_with_scores if s >= threshold]
    if not relevant:
        return "No relevant movies found. Try rephrasing."
    lines = ["Here is what I found:"]
    for i, (text, meta, score) in enumerate(relevant[:3], 1):
        name = meta.get("name", "Unknown movie")
        lines.append(f"{i}. **{name}** (relevance: {score:.2f})")
        short = text[:200] + "..." if len(text) > 200 else text
        lines.append(f"   {short}")
    return "\n".join(lines)

def get_sources(chunks_with_scores, threshold=0.1):
    sources = []
    for text, meta, score in chunks_with_scores:
        if score >= threshold:
            sources.append({
                "doc_id": meta["doc_id"],
                "name": meta.get("name", ""),
                "score": score,
                "fragment": text[:150] + "..." if len(text) > 150 else text
            })
    return sources