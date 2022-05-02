{
  "name": "New undefined Dataset",
  "interface": {
    "type": "text_entity_relations",
    "entityLabels": [
      {
        "id": "food",
        "displayName": "Food",
        "description": "Edible item."
      },
      {
        "id": "hat",
        "displayName": "Hat",
        "description": "Something worn on the head."
      },
      {
        "id": "age",
        "displayName": "AGE"
      }
    ],
    "relationLabels": [
      {
        "id": "subject",
        "displayName": "Subject"
      }
    ]
  },
  "samples": [
    {
      "_id": "snqydhmew",
      "document": "age > 18.",
      "annotation": {
        "entities": [
          {
            "text": "age",
            "textId": "nt2xq5",
            "label": "age",
            "start": 0,
            "end": 2
          }
        ],
        "relations": [
          {
            "from": "nt2xq5",
            "to": "nt2xq5",
            "label": "subject",
            "color": "#d32f2f"
          }
        ]
      },
      "brush": "complete"
    }
  ]
}
