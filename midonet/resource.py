# vim: tabstop=4 shiftwidth=4 softtabstop=4
# Copyright 2011 Midokura Japan KK
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

class ResourceBase(object):

    def accept(self, client, path):
        self.path = path
        self.cl = client
        return self

    def create(self, body):
        assert body != None
        return self.cl.post(self.path, body)

    def list(self):
        return self.cl.get(self.path)

    def get(self, id_):
       path = self.path + '/' + id_
       return self.cl.get(path)

    def delete(self, id_):
        path = self.path + '/' + id_
        return self.cl.delete(path)
