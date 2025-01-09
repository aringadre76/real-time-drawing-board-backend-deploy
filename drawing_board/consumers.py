from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DrawingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "drawing_room"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            x = data.get("x")
            y = data.get("y")
            prevX = data.get("prevX")  # Add previous X coordinate
            prevY = data.get("prevY")  # Add previous Y coordinate
            action = data.get("action")
            clientId = data.get("clientId")  # Add clientId

            # Handle disconnect test
            if action == "disconnect_test":
                await self.close()
                return

            # Validate input
            if not all(key in data for key in ("x", "y", "action")):
                await self.send(text_data=json.dumps({
                    "error": "Invalid payload, unknown keys"
                }))
                return

            # Broadcast valid drawing data
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "broadcast_drawing",
                    "x": x,
                    "y": y,
                    "prevX": prevX,  # Include previous coordinates
                    "prevY": prevY,
                    "action": action,
                    "clientId": clientId,  # Include clientId
                }
            )
        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                "error": "Invalid JSON format"
            }))

    async def broadcast_drawing(self, event):
        await self.send(text_data=json.dumps({
            "x": event["x"],
            "y": event["y"],
            "prevX": event["prevX"],  # Include previous coordinates
            "prevY": event["prevY"],
            "action": event["action"],
            "clientId": event["clientId"],  # Include clientId
        }))