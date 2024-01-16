def open_doc_to_text(doc) -> str:
    return "Question: {}\nAnswer:".format(
        doc["QUESTION"],
    )

def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])
    return "Abstract: {}\nQuestion: {}\nAnswer:".format(
        ctxs,
        doc["QUESTION"],
    )
