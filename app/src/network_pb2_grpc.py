# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import network_pb2 as network__pb2


class NetworkStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SaveImage = channel.unary_unary(
        '/protobuf.Network/SaveImage',
        request_serializer=network__pb2.SaveImageRequest.SerializeToString,
        response_deserializer=network__pb2.SaveImageResponse.FromString,
        )
    self.GetImage = channel.unary_unary(
        '/protobuf.Network/GetImage',
        request_serializer=network__pb2.GetImageRequest.SerializeToString,
        response_deserializer=network__pb2.GetImageResponse.FromString,
        )
    self.CreateUser = channel.unary_unary(
        '/protobuf.Network/CreateUser',
        request_serializer=network__pb2.CreateUserRequest.SerializeToString,
        response_deserializer=network__pb2.CreateUserResponse.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/protobuf.Network/GetUser',
        request_serializer=network__pb2.GetUserRequest.SerializeToString,
        response_deserializer=network__pb2.GetUserResponse.FromString,
        )
    self.SearchForUser = channel.unary_unary(
        '/protobuf.Network/SearchForUser',
        request_serializer=network__pb2.SearchForUserRequest.SerializeToString,
        response_deserializer=network__pb2.SearchForUserResponse.FromString,
        )
    self.CreateFriendship = channel.unary_unary(
        '/protobuf.Network/CreateFriendship',
        request_serializer=network__pb2.CreateFriendshipRequest.SerializeToString,
        response_deserializer=network__pb2.CreateFriendshipResponse.FromString,
        )
    self.ReplyToFriendship = channel.unary_unary(
        '/protobuf.Network/ReplyToFriendship',
        request_serializer=network__pb2.ReplyToFriendshipRequest.SerializeToString,
        response_deserializer=network__pb2.ReplyToFriendshipResponse.FromString,
        )
    self.SubmitItem = channel.unary_unary(
        '/protobuf.Network/SubmitItem',
        request_serializer=network__pb2.SubmitItemRequest.SerializeToString,
        response_deserializer=network__pb2.SubmitItemResponse.FromString,
        )
    self.SubmitItemOffer = channel.unary_unary(
        '/protobuf.Network/SubmitItemOffer',
        request_serializer=network__pb2.SubmitItemOfferRequest.SerializeToString,
        response_deserializer=network__pb2.SubmitItemOfferResponse.FromString,
        )
    self.CreateNetwork = channel.unary_unary(
        '/protobuf.Network/CreateNetwork',
        request_serializer=network__pb2.CreateNetworkRequest.SerializeToString,
        response_deserializer=network__pb2.CreateNetworkResponse.FromString,
        )
    self.GetNetworksForUser = channel.unary_unary(
        '/protobuf.Network/GetNetworksForUser',
        request_serializer=network__pb2.GetNetworksForUserRequest.SerializeToString,
        response_deserializer=network__pb2.GetNetworksForUserResponse.FromString,
        )
    self.GetItemsForUser = channel.unary_unary(
        '/protobuf.Network/GetItemsForUser',
        request_serializer=network__pb2.GetItemsForUserRequest.SerializeToString,
        response_deserializer=network__pb2.GetItemsForUserResponse.FromString,
        )
    self.GetItemsForNetwork = channel.unary_unary(
        '/protobuf.Network/GetItemsForNetwork',
        request_serializer=network__pb2.GetItemsForNetworkRequest.SerializeToString,
        response_deserializer=network__pb2.GetItemsForNetworkResponse.FromString,
        )
    self.SearchForNetworks = channel.unary_unary(
        '/protobuf.Network/SearchForNetworks',
        request_serializer=network__pb2.SearchForNetworksRequest.SerializeToString,
        response_deserializer=network__pb2.SearchForNetworksResponse.FromString,
        )
    self.InviteUserToNetwork = channel.unary_unary(
        '/protobuf.Network/InviteUserToNetwork',
        request_serializer=network__pb2.InviteUserToNetworkRequest.SerializeToString,
        response_deserializer=network__pb2.InviteUserToNetworkResponse.FromString,
        )
    self.ReplyToNetworkInvite = channel.unary_unary(
        '/protobuf.Network/ReplyToNetworkInvite',
        request_serializer=network__pb2.ReplyToNetworkInviteRequest.SerializeToString,
        response_deserializer=network__pb2.ReplyToNetworkInviteResponse.FromString,
        )


class NetworkServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SaveImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetImage(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchForUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateFriendship(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplyToFriendship(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubmitItem(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubmitItemOffer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateNetwork(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNetworksForUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetItemsForUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetItemsForNetwork(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchForNetworks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InviteUserToNetwork(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplyToNetworkInvite(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_NetworkServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SaveImage': grpc.unary_unary_rpc_method_handler(
          servicer.SaveImage,
          request_deserializer=network__pb2.SaveImageRequest.FromString,
          response_serializer=network__pb2.SaveImageResponse.SerializeToString,
      ),
      'GetImage': grpc.unary_unary_rpc_method_handler(
          servicer.GetImage,
          request_deserializer=network__pb2.GetImageRequest.FromString,
          response_serializer=network__pb2.GetImageResponse.SerializeToString,
      ),
      'CreateUser': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUser,
          request_deserializer=network__pb2.CreateUserRequest.FromString,
          response_serializer=network__pb2.CreateUserResponse.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=network__pb2.GetUserRequest.FromString,
          response_serializer=network__pb2.GetUserResponse.SerializeToString,
      ),
      'SearchForUser': grpc.unary_unary_rpc_method_handler(
          servicer.SearchForUser,
          request_deserializer=network__pb2.SearchForUserRequest.FromString,
          response_serializer=network__pb2.SearchForUserResponse.SerializeToString,
      ),
      'CreateFriendship': grpc.unary_unary_rpc_method_handler(
          servicer.CreateFriendship,
          request_deserializer=network__pb2.CreateFriendshipRequest.FromString,
          response_serializer=network__pb2.CreateFriendshipResponse.SerializeToString,
      ),
      'ReplyToFriendship': grpc.unary_unary_rpc_method_handler(
          servicer.ReplyToFriendship,
          request_deserializer=network__pb2.ReplyToFriendshipRequest.FromString,
          response_serializer=network__pb2.ReplyToFriendshipResponse.SerializeToString,
      ),
      'SubmitItem': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitItem,
          request_deserializer=network__pb2.SubmitItemRequest.FromString,
          response_serializer=network__pb2.SubmitItemResponse.SerializeToString,
      ),
      'SubmitItemOffer': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitItemOffer,
          request_deserializer=network__pb2.SubmitItemOfferRequest.FromString,
          response_serializer=network__pb2.SubmitItemOfferResponse.SerializeToString,
      ),
      'CreateNetwork': grpc.unary_unary_rpc_method_handler(
          servicer.CreateNetwork,
          request_deserializer=network__pb2.CreateNetworkRequest.FromString,
          response_serializer=network__pb2.CreateNetworkResponse.SerializeToString,
      ),
      'GetNetworksForUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetNetworksForUser,
          request_deserializer=network__pb2.GetNetworksForUserRequest.FromString,
          response_serializer=network__pb2.GetNetworksForUserResponse.SerializeToString,
      ),
      'GetItemsForUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetItemsForUser,
          request_deserializer=network__pb2.GetItemsForUserRequest.FromString,
          response_serializer=network__pb2.GetItemsForUserResponse.SerializeToString,
      ),
      'GetItemsForNetwork': grpc.unary_unary_rpc_method_handler(
          servicer.GetItemsForNetwork,
          request_deserializer=network__pb2.GetItemsForNetworkRequest.FromString,
          response_serializer=network__pb2.GetItemsForNetworkResponse.SerializeToString,
      ),
      'SearchForNetworks': grpc.unary_unary_rpc_method_handler(
          servicer.SearchForNetworks,
          request_deserializer=network__pb2.SearchForNetworksRequest.FromString,
          response_serializer=network__pb2.SearchForNetworksResponse.SerializeToString,
      ),
      'InviteUserToNetwork': grpc.unary_unary_rpc_method_handler(
          servicer.InviteUserToNetwork,
          request_deserializer=network__pb2.InviteUserToNetworkRequest.FromString,
          response_serializer=network__pb2.InviteUserToNetworkResponse.SerializeToString,
      ),
      'ReplyToNetworkInvite': grpc.unary_unary_rpc_method_handler(
          servicer.ReplyToNetworkInvite,
          request_deserializer=network__pb2.ReplyToNetworkInviteRequest.FromString,
          response_serializer=network__pb2.ReplyToNetworkInviteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protobuf.Network', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
