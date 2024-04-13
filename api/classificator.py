from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image

labels_raw = ['Drivers1', 'Drivers2', 'Passports1', 'Passports2', 'PTS', 'STS1', 'STS2']
labels_to_ids = {
    label: i for label, i in zip(
        labels_raw, range(len(labels_raw))
    )
}
ids_to_labels = {
    i: label for label, i in zip(
        labels_raw, range(len(labels_raw))
    )
}

processor = AutoImageProcessor.from_pretrained("microsoft/swinv2-base-patch4-window8-256")
model = AutoModelForImageClassification.from_pretrained(
    "model",
    num_labels=len(labels_to_ids),
    id2label=ids_to_labels,
    label2id=labels_to_ids,
    ignore_mismatched_sizes=True
)


def get_class_and_proba(image: Image) -> (str, float):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    return model.config.id2label[predicted_class_idx], float(logits.max().detach().numpy())
